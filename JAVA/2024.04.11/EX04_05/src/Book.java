public class Book {
	String title;
	String author;
	void show() { System.out.println(title + " " + author); }

	public Book() {
		this("", "");
		System.out.println("생성자 호출됨");
	}
	public Book(String title) {
		this(title, "작자미상");
	}
	public Book(String title, String author) {
		this.title = title; this.author = author;
	}
	public static void main(String [] args) {
		@SuppressWarnings("unused")				//에러 없애기 위해 넣음
		Book javaBook = new Book("어린왕자", "생떽쥐베리");
		Book bible = new Book("춘향전");
		@SuppressWarnings("unused")				//에러 없애기 위해 넣음
		Book emptyBook = new Book();
		bible.show();
	}
}
