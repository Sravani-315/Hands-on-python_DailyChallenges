This project is a **Doraemon Smart Transport System** that simulates package loading using weight classification and a **Personalized Loading Impact (PLI)** rule based on a user’s name.

The program accepts multiple package weights, validates them, classifies them into loading categories, and then applies Doraemon’s **PLI magic rule** to modify the final loading plan.

---

## Personalization Details

* **Name used:** Sravani  
* **Length of name – L value:** 7  
* **PLI Calculation:** `PLI = L % 3`  
* **PLI Value:** 1  

---

## Applied Personalization Rule

Since **PLI = 1**, the rule applied is:

 **All packages in the "Very Light" category are removed from the loading plan.**  
These removed packages are counted as **affected packages due to PLI**.

---

## Package Classification Rules

Packages are classified based on their weights:

* **Very Light:** ≤ 5  
* **Normal Load:** 6 – 25  
* **Heavy Load:** 26 – 60  
* **Overload:** > 60  
* **Invalid Entries:** Negative weights  

---

## What the Program Produces

After entering the package weights, the system displays:

* Name length (L) and PLI value
* Total valid package entries
* Number of packages affected by PLI
* Final loading categories:
  * Very Light
  * Normal Load
  * Heavy Load
  * Overload
* Invalid weight entries
