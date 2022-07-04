#ARG IMAGE=containers.intersystems.com/intersystems/irishealth-community:2021.2.0.651.0
ARG IMAGE=intersystemsdc/iris-community
#ARG IMAGE=intersystemsdc/iris-community:preview
FROM $IMAGE

# For non community version
# COPY key/iris.key /usr/irissys/mgr/iris.key
USER root

# Update package and install sudo
RUN apt-get update && apt-get install -y \
	nano \
	python3-pip \
	python3-venv \
	sudo && \
	/bin/echo -e ${ISC_PACKAGE_MGRUSER}\\tALL=\(ALL\)\\tNOPASSWD: ALL >> /etc/sudoers && \
	sudo -u ${ISC_PACKAGE_MGRUSER} sudo echo enabled passwordless sudo-ing for ${ISC_PACKAGE_MGRUSER}

# create dev directory
WORKDIR /opt/irisapp
RUN chown ${ISC_PACKAGE_MGRUSER}:${ISC_PACKAGE_IRISGROUP} /opt/irisapp
USER ${ISC_PACKAGE_MGRUSER}

# Copy source files to image
COPY . /opt/irisapp
#COPY  Installer.cls .
# load demo stuff
COPY iris.script /opt/irisapp/iris.script

RUN iris start IRIS \
	&& iris session IRIS < /opt/irisapp/iris.script && iris stop IRIS quietly

# create Python env
ENV PYTHON_PATH=/usr/irissys/bin/irispython
ENV SRC_PATH=/opt/irisapp
ENV IRISUSERNAME "SuperUser"
ENV IRISPASSWORD "SYS"

# Requirement for embedded python
RUN pip3 install -r ${SRC_PATH}/src/Python/requirements.txt
