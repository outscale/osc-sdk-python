export OSC_TEST_PASSWORD=ashita wa dochida
export OSC_TEST_LOGIN=joe
export OSC_SECRET_KEY=0000001111112222223333334444445555555666
export OSC_ACCESS_KEY=11112211111110000000
export OSC_ENDPOINT_API=http://127.0.0.1:3000/api/v1
export OSC_IS_RICOCHET=true

if [ "$#" -eq 0 ]; then

    if [ ! -d "osc-ricochet-2" ]; then
	git clone https://github.com/outscale/osc-ricochet-2
    fi

    cd osc-ricochet-2
    pkill ricochet

    cargo build
    cargo run -- ./ricochet.json > /dev/null  &

    sleep 5

    cd ..

fi

set -e

uvx tox
