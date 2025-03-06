import { CRIS } from "./utility"

export const peakFindingNaive = (s: number[]): number => {
	for (let i = 0; i < s.length; i++) {
		if (i == 0 && s[i] >= s[i + 1]) return s[i]
		else if (i == s.length - 1 && s[i] >= s[i - 1]) return s[i]
		else if (s[i] >= s[i - 1] && s[i] >= s[i + 1]) return s[i]
	}
	return -1
}

export const testPeakFindingNaive = (repeat = 10) => {
	console.time()
	for (let i = 0; i < repeat; i++) {
		const s = CRIS()
		// console.log("sequence: ", s)
		const res = peakFindingNaive(s)
		// console.log(res)
	}
	console.log(peakFindingNaive([0, 2])) // check edge case
	console.timeEnd()
}

export const peakFindingRecursion = (s: number[]): number => {
	const mid = Math.floor(s.length / 2)
	if (s[mid] < s[mid - 1]) return peakFindingRecursion(s.slice(0, mid))
	else if (s[mid] < s[mid + 1]) return peakFindingRecursion(s.slice(mid + 1, s.length))
	else return s[mid]
}

export const testPeakFindingRecursion = (repeat = 10) => {
	console.time()
	for (let i = 0; i < repeat; i++) {
		const s = CRIS()
		// console.log("sequence: ", s)
		const res = peakFindingRecursion(s)
		// console.log(res)
	}
	console.log(peakFindingRecursion([0, 2])) // check edge case
	console.timeEnd()
}

export const peakFinding2DNaive = (mat: number[][], row = 0, col = 0): number => {
	let bestRow = row, bestCol = col
	if (row != 0 && mat[row - 1][col] > mat[row][col]) return peakFinding2DNaive(mat, row - 1, col)
	else if (col != 0 && mat[row][col - 1] > mat[row][col]) return peakFinding2DNaive(mat, row, col - 1)
}
