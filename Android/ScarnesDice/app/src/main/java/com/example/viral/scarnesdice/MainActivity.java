package com.example.viral.scarnesdice;

import android.content.Context;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import java.util.Random;

public class MainActivity extends AppCompatActivity {
    public int userCurrentScore = 0;
    public int userOverallScore = 0;
    public int compOverallScore = 0;
    public int compCurrentScore = 0;
    public int userRolls = 0;
    public boolean userTurn = true;
    public boolean compTurn = false;
    Handler handler = new Handler(Looper.getMainLooper());

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void updateUserScore(View v) {
        TextView t = findViewById(R.id.userScore);
        TextView t2 = findViewById(R.id.UserCurrentScore);

        if (userTurn) {
            //t.setText("Score " + (userCurrentScore + userOverallScore));
            //userOverallScore = userCurrentScore + userOverallScore;
            t2.setText("User Current Score " + (userCurrentScore));
        } else {
            t.setText("User Overall Score " + userOverallScore);
        }
    }

    public void updateCompScore(View v) {
        TextView t = findViewById(R.id.computerScore);
        TextView t2 = findViewById(R.id.computerCurrentScore);
        if (compTurn) {
            //t.setText("Score " + (compCurrentScore + compOverallScore));
            t2.setText("Computer Current Score" + compCurrentScore);
        } else {
            t.setText("Computer Overall Score " + compOverallScore);
        }
    }

    public void updateScore(View v) {
        if (userTurn) {
            updateUserScore(v);
        } else {
            updateCompScore(v);
        }
    }

    public void hold(View v) {
        TextView t = findViewById(R.id.userScore);
        TextView t2 = findViewById(R.id.computerScore);
        if (userTurn) {
            userOverallScore = userCurrentScore + userOverallScore;
            t.setText("User Overall Score " + userOverallScore);
            changeTurns(v);
        } else {
            compOverallScore = compOverallScore + compCurrentScore;
            t2.setText("Computer Overall Score " + compOverallScore);
            changeTurns(v);
        }
    }

    public void reset(View v) {
        TextView t = findViewById(R.id.userScore);
        TextView t2 = findViewById(R.id.computerScore);
        TextView t3 = findViewById(R.id.computerCurrentScore);
        TextView t4 = findViewById(R.id.UserCurrentScore);
        userOverallScore = 0;
        compOverallScore = 0;
        userCurrentScore = 0;
        compCurrentScore = 0;
        userTurn = true;
        compTurn = false;
        updateCompScore(v);
        updateUserScore(v);
        ImageView diceRolledImage = findViewById(R.id.diceImage);
        t.setText("User Overall Score " + userOverallScore);
        t2.setText("Computer Overall Score " + compOverallScore);
        t3.setText("Computer Current Score" + compCurrentScore);
        t4.setText("Computer Current Score" + userCurrentScore);
        diceRolledImage.setImageResource(R.drawable.dice1);
    }

    public void changeTurns(View v) {
        Button r = findViewById(R.id.roll);
        Button h = findViewById(R.id.hold);
        Button rs = findViewById(R.id.reset);


        if (userTurn) {
            userTurn = false;
            compTurn = true;
            r.setEnabled(false);
            rs.setEnabled(false);
            h.setEnabled(false);
            compTurn(v);
            compCurrentScore = 0;

        } else {
            compTurn = false;
            userTurn = true;
            r.setEnabled(true);
            h.setEnabled(true);
            rs.setEnabled(true);
            userCurrentScore = 0;
        }
        // userRolls = Integer.parseInt(Rolls.toString());

    }

    public void compTurn(final View v) {

        handler.postDelayed(new Runnable() {
            @Override
            public void run() {
                Context context = getApplicationContext();
                CharSequence text = "Computer scored 1";
                int duration = Toast.LENGTH_SHORT;
                Toast toast = Toast.makeText(context, text, duration);
                Random rand = new Random();
                int state = 0;
                //do {
                state = rand.nextInt(7) + 1;
                if (state >= 1 && state < 7) {
                    if (state == 1) {
                        toast.show();
                    }
                    updateStatus(v, state);

                } else if (state == 7) {
                    hold(v);
                }
                if (state != 1 && state != 7) {
                    compTurn(v);
                }

            }
        }, 1000);
    }

    public void updateStatus(View roll, int imageNum) {
        ImageView diceRolledImage = findViewById(R.id.diceImage);
        switch (imageNum) {
            case 1:
                diceRolledImage.setImageResource(R.drawable.dice1);
                if (userTurn) {
                    userCurrentScore = 0;
                    //userOverallScore = 0;

                } else {
                    compCurrentScore = 0;
                    //compOverallScore = 0;
                }
                //hold(roll);
                updateScore(roll);
                changeTurns(roll);
                break;
            case 2:
                diceRolledImage.setImageResource(R.drawable.dice2);

                if (userTurn) {
                    userCurrentScore += 2;
                } else {
                    compCurrentScore += 2;
                }
                updateScore(roll);
                break;
            case 3:
                diceRolledImage.setImageResource(R.drawable.dice3);
                if (userTurn) {
                    userCurrentScore += 3;
                } else {
                    compCurrentScore += 3;
                }
                updateScore(roll);
                break;
            case 4:
                diceRolledImage.setImageResource(R.drawable.dice4);
                if (userTurn) {
                    userCurrentScore += 4;
                } else {
                    compCurrentScore += 4;
                }
                updateScore(roll);
                break;
            case 5:
                diceRolledImage.setImageResource(R.drawable.dice5);
                if (userTurn) {
                    userCurrentScore += 5;
                } else {
                    compCurrentScore += 5;
                }
                updateScore(roll);
                break;
            case 6:
                diceRolledImage.setImageResource(R.drawable.dice6);
                if (userTurn) {
                    userCurrentScore += 6;
                } else {
                    compCurrentScore += 6;
                }
                updateScore(roll);
                break;
        }
    }

    public void rollDice(View roll) {
        ImageView diceRolledImage = findViewById(R.id.diceImage);
        Random random = new Random();
        int imageNumber = random.nextInt(5) + 1;
        updateStatus(roll, imageNumber);


    }


}
