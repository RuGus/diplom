# Декларация шагов пайплайна
SIMPLE_SGN = ("sign_file", (None,))
SIMPLE_ENC = ("encrypt_file", (None,))
SIMPLE_PACK = ("pack_file", (None,))

PIPELINES = {
    "pack_sgn_enc": (SIMPLE_PACK, SIMPLE_SGN, SIMPLE_ENC),
    "pack_enc": (SIMPLE_PACK, SIMPLE_ENC),
}
