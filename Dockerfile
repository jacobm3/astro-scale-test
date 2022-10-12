FROM quay.io/astronomer/astro-runtime:6.0.2

# ARG DEBIAN_FRONTEND=noninteractive

# USER root
# RUN apt-get update && apt-get -qq install tcpdump
# RUN chmod u+s /usr/bin/tcpdump
# USER astro
