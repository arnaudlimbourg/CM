from django.contrib import admin

from members.models import Member, Team, MemberTeam

admin.site.register(Member)
admin.site.register(Team)
admin.site.register(MemberTeam)