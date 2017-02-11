package com.example.rohanpatel.ptrack;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Button button1 = (Button) findViewById(R.id.button1);

        button1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //Toast.makeText(MainActivity.this, "This is an alert", Toast.LENGTH_SHORT).show();
                Intent intent = new Intent(MainActivity.this, FormOne.class);
                startActivityForResult(intent, 200);
            }
        });
        //button1.setText("Number 1");
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        // Check which request we're responding to
        if (requestCode == 200) {
            // Make sure the request was successful
            if (resultCode == RESULT_OK) {
                Bundle bundle = data.getExtras();
                Toast.makeText(MainActivity.this, bundle.getString("text"), Toast.LENGTH_LONG).show();
            }
        }
    }
}
