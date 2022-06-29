-- FIT DATABASE UNDERGRADUATE UNITS ASSIGNMENT 2 / S1 / 2019
-- FILL IN THE FOLLOWING:
--Unit Code: FIT3171
--Student ID: 28390121
--Student Full Name: Priscilla Tham Ai Ching
--Student email: ptha0007@student.monash.edu
--Tutor Name: Ahmed Shifaz

/*  --- COMMENTS TO YOUR MARKER --------

when dropping tables after running every ALL TASKS,
uncomment new tables in task 1.2.




*/

--Q1
/*
TASK 1.1 BELOW
*/
---------- VEHICLE_UNIT ----------
CREATE TABLE vehicle_unit (
    garage_code             NUMERIC(2) NOT NULL,
    vunit_id                NUMERIC(6) NOT NULL,
    vunit_purchase_price    NUMERIC(7,2) NOT NULL,
    vunit_exhibition_flag   CHAR(1) NOT NULL,
    vehicle_insurance_id    VARCHAR(20) NOT NULL,
    vunit_rego              VARCHAR(8) NOT NULL
);

ALTER TABLE vehicle_unit ADD CONSTRAINT flag_chk CHECK ( vunit_exhibition_flag IN (
    'Y',
    'N'
    ) );

ALTER TABLE vehicle_unit ADD CONSTRAINT vehicle_unit_pk PRIMARY KEY ( garage_code,
                                                                      vunit_id );
                                                                      
ALTER TABLE vehicle_unit ADD CONSTRAINT vunit_rego_uq UNIQUE ( vunit_rego );

COMMENT ON COLUMN vehicle_unit.garage_code IS 
    'Garage number';
    
COMMENT ON COLUMN vehicle_unit.vunit_id IS
    'Vehicle unit identifier';
    
COMMENT ON COLUMN vehicle_unit.vunit_purchase_price IS
    'The cost of a vehicle unit';

COMMENT ON COLUMN vehicle_unit.vunit_exhibition_flag IS
    'Indicator whether the unit is for rental or exhibition';

COMMENT ON COLUMN vehicle_unit.vehicle_insurance_id IS
    'Insurance identifier of a vehicle unit';
    
COMMENT ON COLUMN vehicle_unit.vunit_rego IS
    'Rego of a vehicle unit';


---------- LOAN ----------
CREATE TABLE loan (
    garage_code                 NUMERIC(2) NOT NULL,
    vunit_id                    NUMERIC(6) NOT NULL,
    loan_date_time              DATE NOT NULL,
    loan_due_date               DATE NOT NULL,
    loan_actual_return_date     DATE,
    renter_no                   NUMERIC(6) NOT NULL
);

ALTER TABLE loan ADD CONSTRAINT loan_pk PRIMARY KEY ( garage_code,
                                                      vunit_id,
                                                      loan_date_time );
                                                      
COMMENT ON COLUMN loan.garage_code IS
    'Garage number';
    
COMMENT ON COLUMN loan.vunit_id IS
    'Vehicle unit identifier';
    
COMMENT ON COLUMN loan.loan_date_time IS
    'Date and time of loan';
    
COMMENT ON COLUMN loan.loan_due_date IS
    'Due date of loan';
    
COMMENT ON COLUMN loan.loan_actual_return_date IS
    'Date of return';
    
COMMENT ON COLUMN loan.renter_no IS
    'Renter identifier';

---------- RESERVE ----------
CREATE TABLE reserve (
    garage_code                 NUMERIC(2) NOT NULL,
    vunit_id                    NUMERIC(6) NOT NULL,
    reserve_date_time_placed    DATE NOT NULL,
    renter_no                   NUMERIC(6) NOT NULL
);

ALTER TABLE reserve ADD CONSTRAINT reserve_pk PRIMARY KEY ( garage_code,
                                                            vunit_id,
                                                            reserve_date_time_placed );
                                                            
COMMENT ON COLUMN reserve.garage_code IS
    'Garage number';
    
COMMENT ON COLUMN reserve.vunit_id IS
    'Vehicle unit identifier';
    
COMMENT ON COLUMN reserve.reserve_date_time_placed IS
    'Date and time of reservation';
    
COMMENT ON COLUMN reserve.renter_no IS
    'Renter identifier';


---------- ALTER FKS ----------
ALTER TABLE vehicle_unit
    ADD CONSTRAINT garage_vu FOREIGN KEY ( garage_code )
        REFERENCES garage ( garage_code );
ALTER TABLE vehicle_unit
    ADD CONSTRAINT vehicledetail_vu FOREIGN KEY ( vehicle_insurance_id )
        REFERENCES vehicle_detail ( vehicle_insurance_id );

ALTER TABLE loan
    ADD CONSTRAINT vehicleunit_l FOREIGN KEY ( garage_code,
                                               vunit_id )
        REFERENCES vehicle_unit ( garage_code,
                                  vunit_id );
ALTER TABLE loan
    ADD CONSTRAINT renter_l FOREIGN KEY ( renter_no )
        REFERENCES renter ( renter_no );

ALTER TABLE reserve
    ADD CONSTRAINT vehicleunit_r FOREIGN KEY ( garage_code,
                                               vunit_id )
        REFERENCES vehicle_unit ( garage_code,
                                  vunit_id );
ALTER TABLE reserve
    ADD CONSTRAINT renter_r FOREIGN KEY ( renter_no )
        REFERENCES renter ( renter_no );


     
/*
TASK 1.2 BELOW
 
*/
drop table reserve purge;
drop table loan purge;
drop table vehicle_unit purge;
drop table renter purge;
---- new tables created in task 4
drop table garage_manager_collection purge;
drop table collection purge;
---- end of new tables created in task 4
drop table garage purge;
drop table manager purge;
drop table vehicle_feature purge;
drop table feature purge;
drop table vendor_vehicle purge;
drop table vendor purge;
drop table vehicle_detail purge;
drop table manufacturer purge;







--Q2
/*
TASK 2.1 BELOW

*/
insert into vehicle_detail (vehicle_insurance_id, vehicle_title, 
vehicle_classification, vehicle_weekly_rental, vehicle_manufacture_year, 
vehicle_engine_capacity, manufacturer_id)
values ('sports-ute-449-12b', 'Toyota Hilux SR Manual 4x2 MY14', 'S', 
200, to_date('2018', 'yyyy'), NULL, 
(select manufacturer_id
from manufacturer
where manufacturer_name = 'Toyota'));

insert into vehicle_unit (garage_code, vunit_id, vunit_purchase_price, 
vunit_exhibition_flag, vehicle_insurance_id, vunit_rego)
values (
(select garage_code
from garage
where garage_name = 'Caulfield VIC'), 012345, 50000, 'N', 
'sports-ute-449-12b', 
'RD3161');

insert into vehicle_unit (garage_code, vunit_id, vunit_purchase_price, 
vunit_exhibition_flag, vehicle_insurance_id, vunit_rego)
values (
(select garage_code
from garage
where garage_name = 'South Yarra VIC'), 012346, 50000, 'N', 
'sports-ute-449-12b', 
'RD3141');

insert into vehicle_unit (garage_code, vunit_id, vunit_purchase_price, 
vunit_exhibition_flag, vehicle_insurance_id, vunit_rego)
values (
(select garage_code
from garage
where garage_name = 'Melbourne Central VIC'), 0123457, 50000, 'N', 
'sports-ute-449-12b', 
'RD3000');

commit;

/*
TASK 2.2 BELOW

*/
create sequence renter_sequence
start with 10
increment by 1;




/*
TASK 2.3 BELOW

*/
drop sequence renter_sequence;









--Q3
/*
TASK 3.1 BELOW

*/
insert into renter (renter_no, renter_fname, renter_lname, renter_street, 
renter_suburb, renter_postcode, garage_code, renter_email, renter_mobile)
values (
renter_sequence.nextval, 'Van', 'Diesel', '15 Renver Road', 'Clayton', '3168', 
(select garage_code
from garage
where garage_name = 'Caulfield VIC'), 'vandiesel@live.com', '0408582241');









commit;

/*
TASK 3.2 BELOW

*/
insert into reserve (garage_code, vunit_id, reserve_date_time_placed, renter_no)
values (
(select g.garage_code
from vehicle_unit vu join garage g
on vu.garage_code = g.garage_code
where g.garage_name = 'Melbourne Central VIC'),
(select vunit_id
from vehicle_unit vu join garage g
on vu.garage_code = g.garage_code
where g.garage_name = 'Melbourne Central VIC' and 
vu.vehicle_insurance_id = 'sports-ute-449-12b'),
to_date('04/05/2019 1600', 'dd/mm/yyyy hh24;mi'), 
(select renter_no
from renter
where renter_fname = 'Van' and renter_lname = 'Diesel'));









commit;

/*
TASK 3.3 BELOW

*/
insert into loan (garage_code, vunit_id, loan_date_time, loan_due_date, 
loan_actual_return_date, renter_no)
values (
(select r.garage_code
from vehicle_unit vu join reserve r 
on vu.garage_code = r.garage_code and vu.vunit_id = r.vunit_id
where renter_no = (select renter_no
                   from renter
                   where renter_fname = 'Van' and renter_lname = 'Diesel')),
(select r.vunit_id
from vehicle_unit vu join reserve r
on vu.garage_code = r.garage_code
where renter_no = (select renter_no
                   from renter
                   where renter_fname = 'Van' and renter_lname = 'Diesel')),
(select reserve_date_time_placed
from vehicle_unit vu join reserve r
on vu.garage_code = r.garage_code and vu.vunit_id = r.vunit_id
where renter_no = (select renter_no
                   from renter
                   where renter_fname = 'Van' and renter_lname = 'Diesel'))+7 -2/24,
(select reserve_date_time_placed
from vehicle_unit vu join reserve r
on vu.garage_code = r.garage_code and vu.vunit_id = r.vunit_id
where renter_no = (select renter_no
                   from renter
                   where renter_fname = 'Van' and renter_lname = 'Diesel'))+14 -2/24,
NULL,
(select renter_no
from renter
where renter_fname = 'Van' and renter_lname = 'Diesel')
);






commit;
  
/*
TASK 3.4 BELOW

*/
update loan 
set loan_actual_return_date = 
(select to_date(loan_due_date, 'dd/mm/yyyy')
from loan
where renter_no = (select renter_no
                   from renter
                   where renter_fname = 'Van' and renter_lname = 'Diesel'))
where renter_no = (select renter_no
                   from renter
                   where renter_fname = 'Van' and renter_lname = 'Diesel');
                
insert into loan (garage_code, vunit_id, loan_date_time, loan_due_date, 
loan_actual_return_date, renter_no)
values (
(select r.garage_code
from vehicle_unit vu join reserve r 
on vu.garage_code = r.garage_code and vu.vunit_id = r.vunit_id
where renter_no = (select renter_no
                   from renter
                   where renter_fname = 'Van' and renter_lname = 'Diesel')),
(select r.vunit_id
from vehicle_unit vu join reserve r
on vu.garage_code = r.garage_code
where renter_no = (select renter_no
                   from renter
                   where renter_fname = 'Van' and renter_lname = 'Diesel')),
(select loan_due_date
from loan
where renter_no = (select renter_no
                   from renter
                   where renter_fname = 'Van' and renter_lname = 'Diesel')),
(select loan_due_date
from loan
where renter_no = (select renter_no
                   from renter
                   where renter_fname = 'Van' and renter_lname = 'Diesel'))+7 +0/24,
NULL,
(select renter_no
from renter
where renter_fname = 'Van' and renter_lname = 'Diesel')
);





commit;

--Q4
/*
TASK 4.1 BELOW

*/
ALTER TABLE vehicle_unit
ADD vunit_condition CHAR(1);

ALTER TABLE vehicle_unit ADD CONSTRAINT cond_chk CHECK ( vunit_condition IN (
    'M',
    'W',
    'G'
    ) );

COMMENT ON COLUMN vehicle_unit.vunit_condition IS
    'Indicator whether the unit needs maintenance (M) or written off (W) or 
    in good condition (G)';
    
update vehicle_unit
set vunit_condition = 'G';

ALTER TABLE vehicle_unit
MODIFY vunit_condition NOT NULL;






commit;

/*
TASK 4.2 BELOW
*/
ALTER TABLE loan
ADD return_garage_code NUMERIC(2);

COMMENT ON COLUMN loan.return_garage_code IS
    'Return garage number';
    
ALTER TABLE loan
    ADD CONSTRAINT garage_l FOREIGN KEY ( return_garage_code )
        REFERENCES garage ( garage_code );

update loan
set return_garage_code = garage_code
where loan_actual_return_date is not null;
                        




commit;

/*
TASK 4.3 BELOW
*/
        
---------- COLLECTION ----------
CREATE TABLE collection (
    collection_code     CHAR(1) NOT NULL
);

ALTER TABLE collection ADD CONSTRAINT collection_code_chk CHECK ( collection_code IN (
    'A',
    'B',
    'M',
    'S'
    ) );

ALTER TABLE collection ADD CONSTRAINT collection_pk 
PRIMARY KEY ( collection_code );

COMMENT ON COLUMN collection.collection_code IS
    'Collection classification - (A)ll, (B)ike, regular (M)otorcar, or (S)portscar';

---------- manager_collection ----------
CREATE TABLE garage_manager_collection (
    garage_code         NUMERIC(2) NOT NULL,
    man_id              NUMERIC(2) NOT NULL,
    collection_code     CHAR(1) NOT NULL
);

ALTER TABLE garage_manager_collection ADD CONSTRAINT garage_manager_collection_pk 
PRIMARY KEY ( garage_code,
              man_id,
              collection_code );

ALTER TABLE garage_manager_collection
    ADD CONSTRAINT garage_gmc FOREIGN KEY ( garage_code )
        REFERENCES garage ( garage_code );
              
ALTER TABLE garage_manager_collection
    ADD CONSTRAINT manager_gmc FOREIGN KEY ( man_id )
        REFERENCES manager ( man_id );
              
ALTER TABLE garage_manager_collection
    ADD CONSTRAINT collection_gmc FOREIGN KEY ( collection_code )
        REFERENCES collection ( collection_code );
        
COMMENT ON COLUMN garage_manager_collection.collection_code IS
    'Collection classification - (A)ll, (B)ike, regular (M)otorcar, or (S)portscar';

insert into collection (collection_code)
values ('A');

insert into collection (collection_code)
values ('B');

insert into collection (collection_code)
values ('M');

insert into collection (collection_code)
values ('S');

insert into garage_manager_collection (garage_code, man_id, collection_code)
values (
(select garage_code
from garage
where garage_name = 'Caulfield VIC' and man_id = 1),
1,
'A');

insert into garage_manager_collection (garage_code, man_id, collection_code)
values (
(select garage_code
from garage
where garage_name = 'Melbourne Central VIC'),
1,
'S');

insert into garage_manager_collection (garage_code, man_id, collection_code)
values (
(select garage_code
from garage
where garage_name = 'South Yarra VIC' and man_id = 2),
2,
'A');

insert into garage_manager_collection (garage_code, man_id, collection_code)
values (
(select garage_code
from garage
where garage_name = 'Melbourne Central VIC'),
2,
'B');

insert into garage_manager_collection (garage_code, man_id, collection_code)
values (
(select garage_code
from garage
where garage_name = 'Melbourne Central VIC'),
2,
'M');

commit;

ALTER TABLE garage
DROP COLUMN man_id







