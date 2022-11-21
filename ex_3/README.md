**Week 3 Exercises: EIOA: basic theory & calculations**

**Objectives**

+---+------------------------------------------------+
| • | > Understand the format of input-output tables |
+===+================================================+
| • | > Interpret the Leontief inverse               |
+---+------------------------------------------------+
| • | > Calculate the carbon footprint               |
+---+------------------------------------------------+

**Exercises**

A fictitious nation has a very basic national economy consisting of five
sectors, each producing a single type of goods for sale: rice, beef,
electricity, car, and insurance. The following data were obtained from
the nation\'s Bureau of Statistics:

Inter-industry transactions and value added (unit: €/year):

+----------+---------+----------+----------+---------+----------+
| >        | > Rice\ | > Cattle | > Power  | > Car\  | > I      |
| Industry | > farm  | > farm   | > plant  | > maker | nsurance |
| >        |         |          |          |         | >        |
| Products |         |          |          |         |  company |
+==========+=========+==========+==========+=========+==========+
| > Rice   | > 100   | > 1900   | > 0      | > 0     | > 0      |
+----------+---------+----------+----------+---------+----------+
| > Beef   | > 0     | > 1000   | > 0      | > 0     | > 0      |
+----------+---------+----------+----------+---------+----------+
| > Ele    | > 1600  | > 2500   | > 900    | > 1000  | > 4000   |
| ctricity |         |          |          |         |          |
+----------+---------+----------+----------+---------+----------+
| > Car    | > 500   | > 1500   | > 1500   | > 1000  | > 1500   |
+----------+---------+----------+----------+---------+----------+
| > I      | > 300   | > 700    | > 3000   | > 2000  | > 1000   |
| nsurance |         |          |          |         |          |
+----------+---------+----------+----------+---------+----------+
| > Value  | > 2500  | > 2400   | > 9600   | > 16000 | > 8500   |
| > added  |         |          |          |         |          |
+----------+---------+----------+----------+---------+----------+

The value of finished products sold (final consumption,€/year):

+-------------+---------+
| > Rice      | > 3000  |
+=============+=========+
| > Beef      | > 9000  |
+-------------+---------+
| Electricity | > 5000  |
+-------------+---------+
| > Car       | > 14000 |
+-------------+---------+
| Insurance   | > 8000  |
+-------------+---------+

The direct water use and CO2 emissions by sector. (Note: this is the
environmental extension matrix F)

+----------+---------+----------+----------+---------+----------+
|          | > Rice\ | > Cattle | > Power  | > Car\  | > I      |
|          | > farm  | > farm   | > plant  | > maker | nsurance |
|          |         |          |          |         | >        |
|          |         |          |          |         |  company |
+==========+=========+==========+==========+=========+==========+
| > Water  | > 10000 | > 2000   | > 15000  | > 1000  | > 750    |
| > use    |         |          |          |         |          |
| > (L)    |         |          |          |         |          |
+----------+---------+----------+----------+---------+----------+
| CO2      | > 50    | > 500    | > 7500   | > 300   | > 15     |
| e        |         |          |          |         |          |
| missions |         |          |          |         |          |
| (kg)     |         |          |          |         |          |
+----------+---------+----------+----------+---------+----------+

**1. Arrange all data in the format of an input-output table and
calculate total inputs and total outputs for all five sectors.**

> In python, create arrays for all the data (Z, va, y, F), and use them
> to calculate the total inputs (x_in) and total outputs (x_out) for all
> five sectors.

**2. Calculate the direct use of water, CO2 emissions, and wage payment
per 1 € output.**

> In python:
>
> a)From the environmental extension matrix F, calculate the direct use
> of water (f_water),
>
> CO2(f_co2) and wage payment (f_va) per €1 output.
>
> b)Combine the newly created separate data together into a table
> (f_all).

**3. a. Calculate the Leontief Inverse matrix for the nation: L = (I -
A)\^-1**

> **b. How can L be interpreted?**
>
> In python:
>
> a)Calculate the Technical Coefficient Matrix (A) from the transaction
> (Z) and total output (x or
>
> x_out).
>
> b)Calculate the Leontief Inverse matrix for the nation: L = (I --
> A)\^-1.

**4. a. Calculate the total supply chain-wide water consumption to
produce one €1 of insurance**

**b. Why is this more than the water intensity of the insurance
company?**

> In python:

a)Calculate the total supply chain-wide water consumption to produce one
€1 of insurance

> (f_tot_water) using the L matrix.
>
> b)Use the diagonal of the flattened water consumption (f_water) and
> the L matrix to show the
>
> water consumption per process (f_tot_water_p).

c)Compare the sum of **f_tot_water_p** with **f_tot_water** to show it
returns the same result.

**5. What are carbon footprint of the final demand in the nation?**

**a. The nation's carbon footprint**\
(Note: use matrix algebra for the calculations, with *E = fLy*)\
**b. The nation's carbon footprint by finished product**\
(Note: to retain the finished product breakdown, the final demand vector
can be written on a diagonal)\
**c. The nation's carbon footprint traced to producing sectors**\
(Note: to retain the producing sector breakdown, the total intensity
vector can be written on a diagonal)

> More reflection in python:

a)Combine the two methods above to show the nation's carbon footprint by
both finished

> product and producing sectors (EF_co2_p\_exp).
>
> b)Compare the sum of each matrix with EF_co2 to show that the
> calculations are correct. c)Sum the EF_co2_p\_exp matrix across both
> rows and columns and show that the results are comparable with
> EF_co2_exp and EF_co2_p (use the numpy function .isclose() to compare
> float values).
