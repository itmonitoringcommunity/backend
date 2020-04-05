FROM centos:centos7
MAINTAINER smiley-py <itmonitoringcommunity@gmail.com>
LABEL author="oguz burak karagoz" \
	  mail="oguzkaragoz@gmail.com"

RUN yum -y update  && \
yum -y install epel-release && \
yum -y install python && \
yum -y install python-pip && \
yum -y install git && \
yum clean all

# Install Python and Basic Python Tools and Git
RUN git clone "https://github.com/smiley-py/backend.git"
RUN pip install pip --upgrade
RUN pip install -r /backend/requirements.txt

EXPOSE 8080
WORKDIR /backend

CMD ["python", "/backend/manage.py", "runserver", "0.0.0.0:8000"]