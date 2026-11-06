FROM debian:13.7-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        curl=8.14.1-2+deb13u7 \
        nginx=1.26.3-3+deb13u10 \
        git=1:2.47.3-0+deb13u1 \
    && rm -rf /var/lib/apt/lists/* \
    && groupadd user \
    && useradd -rm -d /home/user -s /bin/bash -g user -u 1001 user

USER user

CMD ["sleep", "infinity"]
