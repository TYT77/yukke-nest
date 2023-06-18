FROM rust:1.70.0-bullseye

RUN cargo install cargo-generate wasm-pack && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - &&\
    apt-get install -y nodejs && \
    npm install npm@latest -g

ENV USER=root