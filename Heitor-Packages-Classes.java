/*
Crie dois pacotes baseados nas atribuições de uma empresa e inclua classes neles. Lembre-se de trabalhar com os padrões Java.
*/

package br.com.papelaria.inventorio;

import java.io.*;
import java.util.*;

public class Caneta {
    public static void defineQuantidadeDeCaneta() {
        Scanner cane = new Scanner(System.in);
        System.out.println("Qual a quantidade de caneta?");
        int qntCane = cane.nextInt();
        System.out.println("A quantidade de canetas é: " + qntCane);
    }
}

public class Lapis {
    public static void defineQuantidadeDeLapis() {
        Scanner lap = new Scanner(System.in);
        System.out.println("Qual a quantidade de lápis?");
        int qntLap = lap.nextInt();
        System.out.println("A quantidade de lápis é: " + qntLap); 
    }
}

package br.com.papelaria.conta;

import br.com.papelaria.inventorio.Caneta;
import br.com.papelaria.inventorio.Lapis;

public class Main{
    public static void main(Int[] args) {
        Caneta.defineQuantidadeDeCaneta();
        Lapis.defineQuantidadeDeLapis();
    }
}
