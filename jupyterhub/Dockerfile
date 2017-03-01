FROM jupyterhub/jupyterhub

RUN echo "Acquire::http::Proxy \"https://192.168.200.2:3128/\";" >>/etc/apt/apt.conf  && \
 apt-get update && \
 apt-get install -y curl && \
 apt-get clean && \
 git config --global http.proxy https://192.168.200.2:3128/ && \
 git config --global https.proxy https://192.168.200.2:3128/ && \
 pip install --proxy=https://192.168.200.2:3128/ jupyterhub-ldapauthenticator && \
 #pip install --proxy=https://192.168.200.2:3128/ git+https://github.com/danielfrg/jupyterhub-kubernetes_spawner.git && \
 pip install --proxy=https://192.168.200.2:3128/ git+https://github.com/jbmarcille/kubespawner.git && \
 mkdir -p /srv/jupyterhub/

COPY jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py
WORKDIR /srv/jupyterhub/
LABEL org.jupyter.service="jupyterhub"

CMD ["jupyterhub", "--debug", "--ip", "0.0.0.0", "-f", "/srv/jupyterhub/jupyterhub_config.py"]
