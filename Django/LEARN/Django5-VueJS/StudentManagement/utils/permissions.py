from django.contrib.auth.mixins import AccessMixin
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy

# 定义用户权限


def role_required(*allowed_roles):
    def decorator(view_func):
        def _warpped_view(request, *args, **kwargs):
            # 实现验证
            user_role = request.session.get('user_role')
            if request.user.isauthenticated and user_role in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return JsonResponse({
                    'status': 'error',
                    'messages': '无权限访问'
                }, status=404)
        return _warpped_view
    return decorator


class RoleRequiredMixin(AccessMixin):
    allowed_roles = []

    def dispatch(self, request, *args, **kwargs):
        # 检查是否有用户登录，若没有，返回无权限访问
        if not request.user.is_authenticated:
            return self.handle_no_permission
        # 检查用户角色来判断权限
        user_role = request.session.get('user_role')
        # 若不是admin 或者不在允许访问的用户列表中
        if not (request.user.is_superuser or user_role in self.allowed_roles):
            return HttpResponseRedirect(reverse_lazy('user_login'))

        return super().dispatch(request, *args, **kwargs)
