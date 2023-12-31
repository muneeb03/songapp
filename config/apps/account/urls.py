from django.urls import path, include
from apps.account.views import UserRegistrationView, UserLoginView, UserProfileView, UserChangePasswordView, ForgotPasswordView, NewResetPasswordView, AddFavoriteSong

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name ='profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name ='changepassword'),
    path('forgot-password/', ForgotPasswordView.as_view(), name ='forgotpassword'),
    path('reset-password/<uid>/<token>', NewResetPasswordView.as_view(), name="resetpassword"),
    path('favorite-song/<int:song_id>/', AddFavoriteSong.as_view(), name='add-favorite-song'),
]