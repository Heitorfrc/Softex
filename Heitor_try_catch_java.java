/*
Crie uma situação em que ocorra uma exceção dentro de um código. Utilize try/catch para realizar a captura e tratamento dessa exceção.
*/

public class Main {
    public static void main(String[ ] args) {
      try {
        int[] dados = {0, 1, 2, 3, 4};
        System.out.println(dados[5]);
      } catch (Exception e) {
        System.out.println("Ocorreu o erro: " + e.getMessage());
      }
    }
  }