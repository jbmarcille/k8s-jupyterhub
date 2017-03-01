c = get_config()

from os.path import exists,join
runtime_dir = '/srv/jupyterhub'
ssl_dir = join(runtime_dir, 'ssl')

for jdir in ('ssl', 'db'):
  tmp = join(runtime_dir, jdir)
  if(not exists(jdir)):
    os.makedirs(jdir)

c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.confirm_no_ssl = True
#c.JupyterHub.ssl_key = join(ssl_dir, 'jupyterhub.key')
#c.JupyterHub.ssl_cert = join(ssl_dir, 'jupyterhub.crt')
c.JupyterHub.cookie_secret_file = join(ssl_dir, 'cookie_secret')
c.JupyterHub.db_url = join(runtime_dir, 'db', 'jupyterhub.sqlite')
c.JupyterHub.log_level = 'DEBUG'
c.JupyterHub.extra_log_file = join(runtime_dir, 'jupyterhub.log')
c.JupyterHub.debug_db = False
c.JupyterHub.debug_proxy = True

c.Authenticator.admin_users = {'jupyteradmin'}
c.LocalAuthenticator.create_system_users = False
c.JupyterHub.authenticator_class = 'ldapauthenticator.LDAPAuthenticator'
c.LDAPAuthenticator.bind_dn_template = 'uid={username},ou=People,dc=airmes-project,dc=eu'
c.LDAPAuthenticator.allowed_groups = [
  'cn=jupyter,ou=Groups,dc=airmes-project,dc=eu',
]
c.LDAPAuthenticator.server_address = 'ldap'
c.LDAPAuthenticator.server_port = 80
c.LDAPAuthenticator.use_ssl = False

c.Spawner.notebook_dir = '/mnt/jupyterhub/notebooks/{username}'
c.JupyterHub.spawner_class = 'kubernetes_spawner.KubernetesSpawner'
c.KubernetesSpawner.host ='https://kubernetes'
c.KubernetesSpawner.container_image = 'airmes/notebook'
c.KubernetesSpawner.container_port = 8888
#c.KubernetesSpawner.volume_mode = 'glusterfs'
#c.KubernetesSpawner.glusterfs_endpoint = 'glusterfs'
#c.KubernetesSpawner.glusterfs_path = 'brick1'
c.KubernetesSpawner.volume_mode = 'persistent_volume_claim'
c.KubernetesSpawner.persistent_volume_claim_name = 'jupyternotebookclaim'
c.KubernetesSpawner.persistent_volume_claim_path = '/mnt'
c.KubernetesSpawner.verify_ssl = False
c.KubernetesSpawner.hub_ip_from_service = 'jupyterhub'
