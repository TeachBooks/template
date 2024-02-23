FROM continuumio/miniconda3
WORKDIR /book
COPY book/ .
RUN apt-get update && apt-get -y install git gcc
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN jupyter book clean .
RUN jupyter book build .
ENTRYPOINT [ "python", "-m", "http.server", "8000", "--directory", "/book/_build/html"]