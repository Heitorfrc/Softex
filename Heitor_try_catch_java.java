/*
Crie uma situação em que ocorra uma exceção dentro de um código. Utilize try/catch para realizar a captura e tratamento dessa exceção. Em JAVA
*/

public class Main {
    public static void main(String[ ] args) {
      int[] dados = {0, 1, 2, 3, 4};
      try {
        System.out.println(dados[5]);
      } catch (Exception e) {
        System.out.println("Ocorreu o erro: " + e.getMessage());
      }
      try {
        System.out.println(dados[2]/dados[0]);
      } catch (Exception e) {
        System.out.println("Ocorreu o erro: " + e.getMessage());
      }
    }
  }
