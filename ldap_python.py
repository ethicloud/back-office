import ldap
import ldap.modlist
#TODO VARIABILISER
#TODO utiliser les string.format

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

def create_organization(organization):
    dn = "ou="+organization+",dc=ethicloud, dc=local"
    modlist = {
           "objectClass": b"organizationalUnit",
          }
    l.add_s(dn, ldap.modlist.addModlist(modlist))

def get_max_gid(organization):
    groups = get_groups(organization)
    #GID start at 500 in openldap
    gid = 499
    for group in groups:
        current_gid = int(group[1]['gidNumber'][0])
        if current_gid > gid: gid = current_gid
    return gid

def create_group(organization, group):
    dn = "cn="+group+",ou="+organization+",dc=ethicloud, dc=local"
    modlist = {
            "objectClass": b"posixGroup",
            "gidNumber": str(get_max_gid(organization) + 1).encode(),
            }
    l.add_s(dn, ldap.modlist.addModlist(modlist))

def create_user(organization, group, user):
    dn = "cn="+user+",cn="+group+",ou="+organization+",dc=ethicloud, dc=local"
    modlist = {
            "objectClass": b"inetOrgPerson",
            "sn": user.encode(),
            }
    l.add_s(dn, ldap.modlist.addModlist(modlist))

#print(get_groups('seb_company'))
print(get_all_users('seb_company'))

# get admins : 
#print(get_users_in_group('ma_startup', 501))

#get basic users : 
#print(get_users_in_group('ma_startup', 500))

#create_organization("seb_company")
#create_group("seb_company", "service_users")

#print(get_max_gid("tristan_company"))
#create_user("seb_company", "admins", "test_admin")

