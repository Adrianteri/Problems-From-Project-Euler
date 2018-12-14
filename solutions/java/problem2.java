import java.util.Iterator;
import java.util.ArrayList;
import java.util.Iterator;


class Fibonacci
{

    private ArrayList< Integer > evenTermsList = new ArrayList< Integer >();
    private ArrayList< Integer > allTermsList = new ArrayList< Integer >();
    private int evenTermsCount = 0;
    private int s = 0;
    private int ceilingLimit = 4000000;


    public ArrayList< Integer > fib()
    {
        if()
        {
            if(number == 1 || number == 2)
                allTermsList.put(1);

            else
            {
                fib( s - 1 ) + fib( s - 2 );

            }
        
        }

        return allTermsList;

    }
    
    //pick out and count even terms in the fib series
    public int EvenTerms()
    {
        for (int allterm : allTermsList) {
            if(allterm % 2 == 0)
                evenTermsList.put(allterm);
        }

        for (int evenTerm : evenTermsList) {
            count += evenTerm;
            
        }

        return evenTermsCount;

    }

    public void diplay()
    {
        System.out.println( "Count of even Terms for Fibonaccie series less than 4M is : "+count);

    }


    public static void main( String[] Args )
    {

        Fibonacci myFib = new Fibonacci();
        myFib.fib();
        myFib.countEvenTerms();
        myFib.diplay();

    }



}