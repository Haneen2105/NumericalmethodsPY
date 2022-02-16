/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package newton;

import java.util.Scanner;

/**
 *
 * @author Haneen
 */
public class Newton {

    
    
        static float equ(float x){
            float y=1/x;
        return y;
    }
     static float form(float xi[],float point_x,int i){
   float value1;
   int i_sec = i;
    if(i == 0){
         value1 = 1;
         return value1;
    }
    else{
        float value2 = point_x-xi[i-1];
       i_sec--;
        return value2 * form(xi,point_x,i_sec) ;
    }
}
    public static void main(String[] args) {
          Scanner sc = new Scanner(System.in);
        
        
        System.out.println("Please enter the value of x:");
        float point_x = sc.nextFloat();
       
       System.out.println("Please enter the value of the degree:");
        int degree = sc.nextInt();
        int n = degree+1;
        float [][] fx = new float[n][n];
        float [] xi =  new float[n];
     
         System.out.println("Enter xi:");
        for(int i = 0;i<n;i++){
           
            xi[i] = sc.nextFloat();
          
        }
         System.out.println("Enter fx:");
        for (int i = 0;i<n;i++){
           
            fx[0][i] = sc.nextFloat();
        }
  
        for(int i = 1; i < n ; i++){
           for(int j = 0; j < n-i;j++){
               fx[i][j] = ((fx[i-1][j+1])-(fx[i-1][j]))/((xi[j+i])-(xi[j]));
             
           }

        }
         System.out.printf("i\txi\tfx");
         for(int i = 1;i<=degree;i++){
             System.out.printf("\t%d\t",i);
         }
        System.out.println(); 
        for(int i = 0; i<n ;i++){
           System.out.printf("%d\t %.4f \t ", i, xi[i]); 
           for(int j = 0; j<n ;j++){
              
                System.out.printf("%.4f \t ",fx[j][i]); 
           }
            System.out.println(); 
        }
         float y = 0;
        float value;
 for(int i = 0; i < n ; i++){
            y +=  (fx[i][0])* form(xi,point_x,i);
        }
     
       float ans=equ(y);
        System.out.printf("\n ans: %.4f", y);
        System.out.printf("\n ans: %.4f", ans);
        System.out.println();
    }
    
    
    
}
    
    

