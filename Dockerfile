FROM python

# To access 127.0.0.1 from the host, 
# you may need to use the docker command line option: 
# --network="host"
# ENV HOST '127.0.0.1'
# Docker bridge IP
# ENV HOST '172.17.0.2'
# All IPs in Docker and routed to it from the outside in theory
ENV HOST '0.0.0.0'
ENV PORT '8050'
# ENV FHOST '127.0.0.1'
# ENV FHOST '172.17.0.2'
ENV FHOST '0.0.0.0'
ENV FPORT '5000'

EXPOSE ${FPORT} ${PORT}

ENV PIP_ROOT_USER_ACTION=ignore

RUN python3 -m pip install --upgrade pip

# RUN apt update && apt install -y iproute2

ADD requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /app
ADD . /app

CMD ["./start.sh"]
