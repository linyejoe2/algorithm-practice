export const createRandomIntegerSequence = (amount = 10, from = 0, to = 100): number[] => {
	const seq: number[] = []
	const scaleFactor = (to - from + 1)
	for (let i = 0; i < amount; i++) {
		seq.push(Math.floor((Math.random() * scaleFactor) + from))
	}
	return seq
}

export const CRIS = createRandomIntegerSequence

export const createRandomIntegerMatrix = (row = 10, col = 10, from = 0, to = 100): number[][] => {
	const mat: number[][] = []
	for (let i = 0; i < row; i++) {
		mat.push(CRIS(col, from, to))
	}
	return mat
}

export const CRIM = createRandomIntegerMatrix
