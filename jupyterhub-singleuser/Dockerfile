FROM debian:latest

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 PATH=/opt/conda/bin:$PATH

RUN echo "Acquire::http::Proxy \"https://192.168.200.2:3128/\";" >>/etc/apt/apt.conf  && \
 echo "proxy_servers:" >>/root/.condarc && \
 echo "  http: https://192.168.200.2:3128" >>/root/.condarc && \
 echo "  https: https://192.168.200.2:3128" >>/root/.condarc && \
 echo 'export PATH=/opt/conda/bin:$PATH' >/etc/profile.d/conda.sh && \
 apt-get update && \
 apt-get install -y --no-install-recommends curl dpkg bzip2 ca-certificates libxml2-dev libxslt-dev && \
 apt-get clean && \
 rm -rf /var/lib/apt/lists/*  && \
 curl -L0 --proxy https://192.168.200.2:3128 https://repo.continuum.io/miniconda/Miniconda3-4.2.12-Linux-x86_64.sh -o Miniconda3-x64.sh && \
 curl -L0 --proxy https://192.168.200.2:3128 https://github.com/krallin/tini/releases/download/v0.14.0/tini_0.14.0-amd64.deb -o tini_0.14.0-amd64.deb && \
 dpkg -i tini_0.14.0-amd64.deb && \
 rm tini_0.14.0-amd64.deb && \
 /bin/bash Miniconda3-x64.sh -b -p /opt/conda && \
 rm Miniconda3-x64.sh && \
 conda update -y --all -c conda-forge && \
 conda install --quiet --yes -c conda-forge \
  'babel' \
  'bokeh' \
  'bottleneck' \
  'beautifulsoup4' \
  'cloudpickle' \
  'cython' \
  'dill' \
  'h5py' \
  'hdf5' \
  'ipywidgets' \
<<<<<<< HEAD:jupyterhub-singleuser/Dockerfile
=======
  'jupyter' \
>>>>>>> 1f49e5948f325f7c5c36f9b52f15b0c1c3a53d29:Dockerfile
  'jupyterhub' \
  'lxml' \
  'matplotlib' \
  'notebook' \
  'numpy' \
  'numexpr' \
  'pandas' \
  'pandas-datareader' \
  'patsy' \
  'requests' \
  'seaborn' \
  'scipy' \
  'scikit-learn' \
  'scikit-image' \
  'statsmodels' \
  'sqlalchemy' \
  'sympy' \
  'gensim' \
  'vincent' \
  'xlrd' \
  'xlwt' \
  'xlsxwriter' && \
 conda remove --quiet --force -y qt pyqt && \
 conda clean -y -a && \
 jupyter nbextension enable --py widgetsnbextension --sys-prefix && \
 curl -L0 --proxy https://192.168.200.2:3128 https://raw.githubusercontent.com/jbmarcille/k8s-notebook/master/start-singleuser.sh -o /usr/local/bin/start-singleuser.sh && \
 chmod 555 /usr/local/bin/start-singleuser.sh

EXPOSE 8888
ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["sh", "/usr/local/bin/start-singleuser.sh"]
