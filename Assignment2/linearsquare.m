A = [1 0 2; 1 1 0; 0 2 1; 2 1 1]
c = [2; 1; 1; 3]

for i=0:25
    lambda = 0.2 * i
    b = [
        (9*lambda*lambda+58*lambda+87)/(lambda^3 + 18*lambda^2 + 74*lambda+84);
        (6*lambda+9)/(lambda^2+16*lambda+42);
        (8*lambda^2+42*lambda+45)/(lambda^3+18*lambda^2+74*lambda+84)
        ]
    tmp = (A*b-c)
    norm_abc(i+1) = tmp.' * (A * b - c)
    norm_lb(i+1) = (b.' * b)
end

hold on
clear title xlabel ylabel

ax = gca;
ax.XAxisLocation = 'origin';
x = [0:0.2:5];

plot(x, norm_abc, '-x');
plot(x, norm_lb, '-x');

xlabel('\lambda');
legend('$$||Ab-c||_2^2$$', '$$||b||_2^2$$', 'Interpreter', 'latex');
hold off
