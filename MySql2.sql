
SELECT E.ENAME FROM EMPLOYEES E , DEPARTMENTS D WHERE E.DEPTID = (SELECT E.DEPTID FROM EMPLOYEES E WHERE E.EID=108 AND E.DEPTID = D.DEPTID);
