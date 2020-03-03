import ldap

l = ldap.initialize("ldap://ethicloud.local")

l.simple_bind_s("cn=admin,dc=ethicloud,dc=local","JonSn0w")

def get_groups(organization):
    return l.search_s('ou='+organization+',dc=ethicloud,dc=local',
                        ldap.SCOPE_SUBTREE,
                        '(objectclass=posixGroup)',
                        ['cn', 'gidNumber'])

def get_all_users(organization):
    return l.search_s('ou='+organization+',dc=ethicloud,dc=local',
                          ldap.SCOPE_SUBTREE,
                        '(&(objectclass=inetOrgPerson))')

def get_users_in_group(organization, gid):
    return l.search_s('ou='+organization+',dc=ethicloud,dc=local',
                          ldap.SCOPE_SUBTREE,
                        '(&(objectclass=inetOrgPerson)(gidNumber='+str(gid)+'))')

#print(get_groups('ma_startup'))
#print(get_all_users('ma_startup'))

# get admins : 
print(get_users_in_group('ma_startup', 501))

#get basic users : 
print(get_users_in_group('ma_startup', 500))
