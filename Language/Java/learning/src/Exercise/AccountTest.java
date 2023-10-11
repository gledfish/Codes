package Exercise;

import java.util.function.DoubleToLongFunction;

/*
 * ClassName:AccountTest
 * Package:Exercise
 * Project:learning
 * Description:
 * @Create:2023/2/6 - 19:25
 * @author:gled fish
 */
    class Account{
        private int id;
        private double balance;
        private double annualInterestFate;

        public Account(int id, double balance, double annualInterestFate){
            this.id = id;
            this.balance = balance;
            this.annualInterestFate = annualInterestFate;
        }
        public int getId(){
            return this.id;
        }
        public double getBalance(){
            return this.balance;
        }
        public double getAnnualInterestFate(){
            return this.annualInterestFate;
        }
        public void setId(int id){
            this.id = id;
        }
        public void setBalance(double balance){
            this.balance = balance;
        }
        public void setAnnualInterestFate(double annualInterestFate){
            this.annualInterestFate = annualInterestFate ;
        }

        public void withdraw(double amount){
            if(this.balance > amount){
                this.balance -= amount;
                System.out.println("取钱成功");
            } else
                System.out.println("余额不足");
        }

        public void deposit(double amount){
            if(amount > 0){
                this.balance += amount;
                System.out.println("存钱成功");
            } else
                System.out.println("存钱失败！");
        }
}
public class AccountTest {
}
