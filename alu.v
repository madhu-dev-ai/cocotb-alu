module alu (
    input  [3:0] a,
    input  [3:0] b,
    input        op,
    output reg [3:0] result
);

always @(*) begin
    if (op == 0)
        result = a + b;
    else
        result = a - b;
end

endmodule