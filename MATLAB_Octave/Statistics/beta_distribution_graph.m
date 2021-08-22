Z = [0.04 0.05 0.08 0.1 0.2 1 2];
W = 0:0.05:10;
B = zeros(4, 201);
for i = 1:7
    B(i,:) = beta(Z(i),W);
end
plot(W,B)
grid on
legend('$z = 0.04$', '$z = 0.05$', '$z = 0.08$', '$z = 0.1$', '$z = 0.2$', '$z = 1.0$', '$z = 2.0$', 'interpreter', 'latex');
title('Beta function for $z = 0.04, 0.05, 0.08, 0.1, 0.2, 1.0$, and $2.0$', 'interpreter', 'latex');
xlabel('$w$', 'interpreter', 'latex');
ylabel('$B(z,w)$', 'interpreter', 'latex');
