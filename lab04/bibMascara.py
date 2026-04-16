import numpy as np


def fazerMascaraGauss2D(media, desvio):
    """Gera uma mascara gaussiana 2D a partir de media e desvio.

    O comprimento da mascara 1D eh calculado automaticamente por:
    comprimento = 2 * media + 1
    """
    if media < 0:
        raise ValueError("A media deve ser nao negativa.")
    if desvio <= 0:
        raise ValueError("O desvio deve ser maior que zero.")

    comprimento = int(2 * media + 1)
    if comprimento < 1:
        comprimento = 1

    # Eixo centrado na media para montar a gaussiana 1D.
    x = np.arange(comprimento, dtype=float)

    g1d = (1.0 / (desvio * np.sqrt(2.0 * np.pi))) * np.exp(
        -((x - media) ** 2) / (2.0 * desvio ** 2)
    )

    # Normaliza para evitar ganho DC apos a filtragem.
    g1d /= np.sum(g1d)

    # Monta a gaussiana 2D pelo produto externo da 1D com sua transposta.
    wGauss2D = np.outer(g1d, g1d)
    wGauss2D /= np.sum(wGauss2D)

    return wGauss2D
