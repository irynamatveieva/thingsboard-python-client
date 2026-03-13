# Common module -- handwritten code overlaid into each edition during generation.
# When imported as part of an edition package (e.g. tb_ce_client), exposes ThingsboardClient.
# When imported directly from common/ (e.g. in unit tests), the edition modules are absent
# so we skip the export gracefully.
try:
    from .client import ThingsboardClient
    __all__ = ["ThingsboardClient"]
except ImportError:
    pass
