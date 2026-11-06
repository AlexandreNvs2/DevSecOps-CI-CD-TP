FROM debian:latest
RUN apt-get update && apt-get install curl nginx git -y
RUN addgroup user
RUN useradd -rm -d /home/user -s /bin/bash -g user -u 1001 user
CMD ["sleep", "infinity"]
