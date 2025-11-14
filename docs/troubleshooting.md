## ⚠️ Known Issues & Troubleshooting

### UTF-8 errors when reading the API specification

Some users may encounter UTF-8 issues that look like this:

```bash
Problem reading (…)osc_sdk_python/osc-api/outscale.yaml:'ascii' codec can't decode byte 0xe2 in position 14856: ordinal not in range(128)
```

To avoid this issue, configure your locale as follows:

```bash
export LC_ALL=en_US.UTF-8
```

If you do not want your locale to be set system-wide, you can do:

```bash
LC_ALL=en_US.UTF-8 pip install osc-sdk-python
```