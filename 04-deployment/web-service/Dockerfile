# slim python 3.11
# other versions at https://hub.docker.com/_/python/
FROM python:3.11-slim

# working dir inside the container
WORKDIR /app

# requirements
COPY requirements.txt .

# install anaconda and create a new environment
RUN apt-get update && \
    apt-get install -y curl && \
    curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/conda && \
    rm Miniconda3-latest-Linux-x86_64.sh && \
    /opt/conda/bin/conda install -c anaconda flask scikit-learn && \
    /opt/conda/bin/conda install -c conda-forge gunicorn && \
    /opt/conda/bin/conda clean -afy

# Add anaconda to PATH
ENV PATH="/opt/conda/bin:${PATH}"

# copy model and app code to the working directory
COPY lin_reg.bin .
COPY predict.py .

# expose the port on which the app will run
EXPOSE 9696

# set the entry point command for the container
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]