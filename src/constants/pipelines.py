SIMPLE_SGN = ("sgn",)
SIMPLE_ENC = ("enc",)
SIMPLE_PACK = ("pack",)

PIPELINES = {
    "pack_sgn_enc": (SIMPLE_PACK, SIMPLE_SGN, SIMPLE_ENC),
    "pack_enc": (SIMPLE_PACK, SIMPLE_ENC),
}
