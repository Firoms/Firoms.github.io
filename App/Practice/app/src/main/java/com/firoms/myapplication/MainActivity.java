package com.firoms.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    int clickCount = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toast.makeText(getApplicationContext(), "토스트 글자 띄우기!!!!", Toast.LENGTH_LONG).show();
        findViewById(R.id.button).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                clickCount = clickCount + 1;

                Toast.makeText(getApplicationContext(), "clickCount: " + clickCount, Toast.LENGTH_SHORT).show();
            }
        });
    }
}