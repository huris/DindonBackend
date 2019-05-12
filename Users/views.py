import random

from django.db.models import Q

from rest_framework.generics import CreateAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from Users.models import VerifyCode, User
from Users.serializers import SmsCodeSerializer, LoginWithSmsCodeSerializer, UserRegisterSerializer


class SmsCodeView(CreateAPIView):
    """
    获取短信验证码
    """
    queryset = VerifyCode.objects.all()
    serializer_class = SmsCodeSerializer

    def post(self, request, *args, **kwargs):
        is_register = request.data.get('is_register', False)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        mobile = serializer.validated_data['mobile']

        # 生成6位随机验证码
        code = "%04d" % random.randint(0000, 9999)

        # TODO 调用第三方发送短信验证码的接口

        try:
            VerifyCode.objects.create(mobile=mobile,
                                      code=code,
                                      is_register=is_register
                                      )
            return Response({"status": "发送成功"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "发送失败"}, status=status.HTTP_400_BAD_REQUEST)


class LoginWithSmsCodeView(CreateAPIView):
    """
    使用短信验证码登录
    """
    queryset = User.objects.all()
    serializer_class = LoginWithSmsCodeSerializer
    authentication_classes = ()
    permission_classes = ()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.mobile = serializer.validated_data['userPhoneNumber']
        user_query = User.objects.filter(Q(username=self.mobile) | Q(userPhoneNumber=self.mobile))
        if not user_query.count():
            user = self.perform_create(serializer)
        else:
            user = user_query[0]

        token = TokenObtainPairSerializer().get_token(user)
        data = serializer.data
        data.update({'username': user.username})
        data.update({'refresh': str(token)})
        data.update({'access': str(token.access_token)})

        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_200_OK, headers=headers)

    def perform_create(self, serializer):
        return serializer.save(username=self.mobile)


class UserRegisterView(CreateAPIView):
    """
    用户注册
    """
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
