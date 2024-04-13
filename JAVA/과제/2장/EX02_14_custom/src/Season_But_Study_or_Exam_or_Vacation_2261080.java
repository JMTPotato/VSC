import java.util.Scanner;

public class Season_But_Study_or_Exam_or_Vacation2261080 {
    public static void main(String[] args)	{
		Scanner scanner = new Scanner(System.in);

        
		String StudyExamVacation;
		String IFStudyExamVacation;

		System.out.print("월(1~12)을 입력하시오:");
		int month = scanner.nextInt();	//정수로 월 입력
		
		switch(month)	{
			case 3:
            case 5:
            case 9:
            case 11:
                StudyExamVacation = "개강 입니다.";
                break;
			case 4: case 10:
				StudyExamVacation = "중간고사 기간입니다.";
                break;
			case 6: case 12:
				StudyExamVacation = "기말고사 기간입니다."; 
				break;
			case 1: case 2: case 7: case 8:
				StudyExamVacation = "행복한 종강입니다.";
				break;
			default:
				StudyExamVacation = "잘못된 ";
		}
		
		if(month == 3 || month == 5 || month == 9 || month == 11)
			IFStudyExamVacation = "수고하십시오.";
		else if(((month == 4) || (month == 6)) || ((month == 10) || (month == 12)))
			IFStudyExamVacation = "놀지말고 공부하십시오.";
		else if(((month == 1) || (month == 2)) || ((month == 7) || (month == 8)))
			IFStudyExamVacation = "지금을 즐기십시오.";
		else
			IFStudyExamVacation = "입력입니다.";

        System.out.println(month + "월은 " + StudyExamVacation + IFStudyExamVacation);

		scanner.close();
	}
}