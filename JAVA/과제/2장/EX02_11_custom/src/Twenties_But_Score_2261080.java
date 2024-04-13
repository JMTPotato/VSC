import java.util.Scanner;

public class Twenties_But_Score_2261080 {
    public static void main(String[] args)	{
		Scanner scanner = new Scanner(System.in);
		
		System.out.print("성적을 입력하시오: ");
		int score = scanner.nextInt();
		
		if((score>=80) && (score<90))	{					//score가 80이상 100미만으로 나오면 B
			System.out.print("시험 등급은 B 입니다. ");
			System.out.println("더 공부했으면 A인데 안타깝네요.");
		}
		else
			System.out.println("시험 등급이 B는 아닙니다. A일수도 F일수도 있습니다.");
		
		scanner.close();
	}
}

//20대 판별기에서 시험등급 B판톡기로 변경, A로 하게되면 if문에서 score가 90보다 높으면 A등급이라 할 수 있기에 사이 값을 하기 좋은 B등급을 가지고 코드를 수정하였습니다.