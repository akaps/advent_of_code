import aoc2019.day19.tractor_beam as beam

def sample_grid():
    grid = {}
    grid[(0, 0)] = beam.PULLED
    grid[(1, 0)] = beam.STATIONARY

    grid[(1, 1)] = beam.PULLED

    grid[(2, 2)] = beam.PULLED
    grid[(3, 2)] = beam.PULLED

    grid[(3, 3)] = beam.PULLED
    grid[(4, 3)] = beam.PULLED
    grid[(5, 3)] = beam.PULLED

    grid[(4, 4)] = beam.PULLED
    grid[(5, 4)] = beam.PULLED
    grid[(6, 4)] = beam.PULLED

    grid[(5, 5)] = beam.PULLED
    grid[(6, 5)] = beam.PULLED
    grid[(7, 5)] = beam.PULLED
    grid[(8, 5)] = beam.PULLED

    grid[(6, 6)] = beam.PULLED
    grid[(7, 6)] = beam.PULLED
    grid[(8, 6)] = beam.PULLED
    grid[(9, 6)] = beam.PULLED

    grid[(6, 7)] = beam.PULLED
    grid[(7, 7)] = beam.PULLED
    grid[(8, 7)] = beam.PULLED
    grid[(9, 7)] = beam.PULLED

    grid[(7, 8)] = beam.PULLED
    grid[(8, 8)] = beam.PULLED
    grid[(9, 8)] = beam.PULLED

    grid[(8, 9)] = beam.PULLED
    grid[(9, 9)] = beam.PULLED
    return grid

def test_sample_grid():
    sample = sample_grid()
    assert beam.count_pulled(sample) == 27
