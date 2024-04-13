import java.io.PrintStream;

public class LogicalOperator_2261080 {
    @SuppressWarnings("all")		//모든 노란줄 경고 무시
    public static void main (String[] args) {
		/*
        System.out.println('a' > 'b');              //false
		System.out.println(3 >= 2);                 //true
		System.out.println(-1 < 0);                 //true
		System.out.println(3.45 <= 2);              //false
		System.out.println(3 == 2);                 //false
		System.out.println(3 != 2);                 //true
		System.out.println(!(3 != 2));              //false
		System.out.println((3 > 2) && (3 > 4));     //false
		System.out.println((3 != 2) || (-1 > 0));   //true
		System.out.println((3 != 2) ^ (-1 > 0));    //true
        */

        PrintStream out = System.out;
        out.println('@' > '(');              //True //@가 64, (가 40
		out.println(25 >= 25);               //true //앞이 뒤보다 크거나 같다.
		out.println(8 < 8);                  //false
		out.println(3.45 <= 3.46);           //true
		out.println(5 == 5);                 //true
		out.println(5 != 5);                 //false
		out.println(!(5 != 5));              //true
		out.println((3 > 2) && (3 > 4));     //false //and연산으로 a,b모두 같은 경우만 true
		out.println((3 != 2) || (-1 > 0));   //true //or연산으로, a,b 모두 false 일 때 false
		out.println((3 != 2) ^ (-1 > 0));    //true //xor연산으로 a,b가 같으면 false
        //                   true       false
        out.println(((5 >= 5) ^ (10 != -10)) || (':' > '_'));   //false //전체 응용하여 만든 코드
        //             true 		true  			
		//                   false       		 false		= false
    }                      
}

//비교, 논리 연산자 사용에 더 적응 하고 참과 거짓 중 어떤 값이 나오는지 확실하게 예상하기 위해 값을 변경하여 연습하였습니다.
//주석처리 되어 있는 것이 원래 예제 그 밑에가 변경한 코드 입니다.








