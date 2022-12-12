import numpy
def transponeeriK(maatriks):
    transponeeritud = numpy.transpose(maatriks)
    vastupidi = transponeeritud[::-1]
    tulemus = numpy.fliplr(vastupidi)
    return tulemus