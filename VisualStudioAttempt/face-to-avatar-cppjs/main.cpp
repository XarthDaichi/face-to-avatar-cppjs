#include <stdio.h>
#include <GL/glew.h>
#include <GL/freeglut.h>


using namespace std;

GLuint VBO;

static void RenderSceneCB() {
	glClear(GL_COLOR_BUFFER_BIT);

	glBindBuffer(GL_ARRAY_BUFFER, VBO);

	glEnableVertexAttribArray(0);

	glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, 0);

	// glDrawArrays(GL_TRIANGLES, 0, 3);

	glDisableVertexAttribArray(0);

	glutSwapBuffers();
}

static void CreateVertexBuffer() {
	glEnable(GL_CULL_FACE);
	glFrontFace(GL_CW);
	glCullFace(GL_FRONT);

}


int main(int argc, char** argv) {
	
	return 0;
}