class SnakeGame {

    /** Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0]. */
    
    Queue<Integer> snake;
    boolean[][] board;
    int[][] food;
    int index;
    int height, width;
    int row, col;
    int score;
    public SnakeGame(int width, int height, int[][] food) {
        this.board = new boolean[height][width];
        this.food = food;
        this.index = 0;
        this.snake = new LinkedList<>();
        this.snake.offer(0);
        this.height = height;
        this.width = width;
        this.row = 0;
        this.col = 0;
        this.score = 0;
    }
    
    /** Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body. */
    public int move(String direction) {
        if (score == -1)
            return score;
        if (direction.equals("U"))
            row--;
        else if (direction.equals("D"))
            row++;
        else if (direction.equals("L"))
            col--;
        else if (direction.equals("R"))
            col++;
        // cross boundary
        if (row < 0 || col < 0 || row >= height || col >= width) {
            score = -1;
            return score;
        }
        // not food
        if (index == food.length || !(row == food[index][0] && col == food[index][1])) {
            int temp = snake.poll();
            board[temp/width][temp%width] = false;
        }   
        else {
            score++;
            index++;
        }
        // bite itself
        if (board[row][col]) {
            score = -1;
            return score;
        }
        else {
            snake.offer(row * width + col);
            board[row][col] = true;
        }
        return score;
    }
}

/**
 * Your SnakeGame object will be instantiated and called as such:
 * SnakeGame obj = new SnakeGame(width, height, food);
 * int param_1 = obj.move(direction);
 */
