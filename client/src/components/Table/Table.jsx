import * as React from "react";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import "./Table.css";


function createData(name, trackingId, date, status) {
  return { name, trackingId, date, status };
}

const rows = [
  createData("Beehive 1", 18908424, "8 November 2022", "Inoperative"),
  createData("Beehive 2", 18908424, "3 September 2022", "Operational"),
  createData("Beehive 3", 18908424, "3 September 2022", "Operational"),
  createData("Beehive 4", 18908421, "3 September 2022", "Operational"),
  createData("Beehive 5", 18908421, "3 September 2022", "Operational"),
  createData("Beehive 6", 18908421, "3 September 2022", "Operational"),
  createData("Beehive 7", 18908421, "3 September 2022", "Operational"),
  createData("Beehive 8", 18908421, "9 November 2022", "Maintenance"),
];


const makeStyle=(status)=>{
  if(status === 'Operational')
  {
    return {
      background: 'rgb(145 254 159 / 47%)',
      color: 'green',
    }
  }
  else if(status === 'Inoperative')
  {
    return{
      background: '#ffadad8f',
      color: 'red',
    }
  }
  else{
    return{
      background: '#59bfff',
      color: 'white',
    }
  }
}

export default function BasicTable() {
  return (
      <div className="Table">
      <h3>Beehives</h3>
        <TableContainer
          component={Paper}
          style={{ boxShadow: "0px 13px 20px 0px #80808029" }}
        >
          <Table sx={{ minWidth: 650 }} aria-label="simple table">
            <TableHead>
              <TableRow>
                <TableCell>Beehive</TableCell>
                <TableCell align="left">Status</TableCell>
                <TableCell align="left">Since</TableCell>

              </TableRow>
            </TableHead>
            <TableBody style={{ color: "white" }}>
              {rows.map((row) => (
                <TableRow
                  key={row.name}
                  sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
                >
                  <TableCell component="th" scope="row">
                    {row.name}
                  </TableCell>
                  <TableCell align="left">
                    <span className="status" style={makeStyle(row.status)}>{row.status}</span>
                  </TableCell>
                  <TableCell align="left">{row.date}</TableCell>

                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </div>
  );
}
