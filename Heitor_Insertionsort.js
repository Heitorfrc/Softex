
var vetor = [17,1,13,21,5,7,19,9,25,33,3,29,41,87,23,49,39,67,43,99,77,55,97,37,35,71,63,51,31,93];

function insertionSort(vetor) {
    let atual;
    for (let i = 1; i<vetor.length; i++) {
        let j = i - 1;
        atual = vetor[i];
        while(j >= 0 && atual< vetor[j]) {
            vetor[j+1] = vetor[j];
            j--;
        }
        vetor[j+1] = atual;
    }
        return vetor;
}
console.log (insertionSort(vetor));
