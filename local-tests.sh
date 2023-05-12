OSC_TEST_PASSWORD=ashita wa dochida
OSC_TEST_LOGIN=joe
OSC_SECRET_KEY=0000001111112222223333334444445555555666
OSC_ACCESS_KEY=11112211111110000000
OSC_ENDPOINT_API=http://127.0.0.1:3000


if [ ! -d "osc-ricochet-2" ]; then
    git clone https://github.com/outscale-mgo/osc-ricochet-2
fi

cd osc-ricochet-2
pkill ricochet

cargo build
cargo run -- ./ricochet.json > /dev/null  &

sleep 5

cd ..

set -e

make test
